"""Offline compatibility checks; no AWS calls or repository formatting."""
import ast
import os
import subprocess
import sys
import tempfile
from pathlib import Path
from unittest.mock import patch
from django.test import SimpleTestCase
from botocore.stub import Stubber
import boto3
import black

class ToolchainUpgradeTests(SimpleTestCase):
    def test_aws_cli_version_and_local_model_validation(self):
        with tempfile.TemporaryDirectory() as directory:
            env = dict(os.environ, AWS_CONFIG_FILE=str(Path(directory)/'config'), AWS_SHARED_CREDENTIALS_FILE=str(Path(directory)/'credentials'), AWS_EC2_METADATA_DISABLED='true', AWS_DEFAULT_REGION='us-east-1', AWS_PAGER='', HOME=directory)
            result = subprocess.run([sys.executable, '-m', 'awscli', '--version'], env=env, capture_output=True, text=True, timeout=20)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn('aws-cli/1.46.2', result.stdout + result.stderr)
            # This command only validates a local model and emits a skeleton.
            result = subprocess.run([sys.executable, '-m', 'awscli', 's3api', 'put-object', '--generate-cli-skeleton', 'input'], env=env, capture_output=True, text=True, timeout=20)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn('Bucket', result.stdout)

    def test_existing_boto_storage_client_remains_compatible(self):
        client = boto3.client('s3', region_name='us-east-1', aws_access_key_id='synthetic-key', aws_secret_access_key='synthetic-secret')
        with Stubber(client) as stubber:
            stubber.add_response('put_object', {'ETag': '"synthetic-etag"'}, {'Bucket': 'test-bucket', 'Key': 'test.txt', 'Body': b'test'})
            self.assertEqual(client.put_object(Bucket='test-bucket', Key='test.txt', Body=b'test')['ETag'], '"synthetic-etag"')
            stubber.assert_no_pending_responses()

    def test_black_preserves_syntax_and_does_not_execute_input(self):
        source = 'def value( ):\n return {"answer":42}\n'
        formatted = black.format_file_contents(source, fast=False, mode=black.Mode())
        self.assertEqual(ast.dump(ast.parse(source)), ast.dump(ast.parse(formatted)))
        with self.assertRaises(black.NothingChanged):
            black.format_file_contents(formatted, fast=False, mode=black.Mode())
        with tempfile.TemporaryDirectory() as directory:
            marker = Path(directory)/'must-not-exist'
            code = f'__import__("pathlib").Path({str(marker)!r}).touch()\n'
            black.format_file_contents(code, fast=False, mode=black.Mode())
            self.assertFalse(marker.exists())
