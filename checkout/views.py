from django.shortcuts import render

def checkout(request):
    if request.method == 'POST':
        # Здесь добавьте логику для обработки данных чекаута и Stripe
        pass
    return render(request, 'checkout/checkout.html')