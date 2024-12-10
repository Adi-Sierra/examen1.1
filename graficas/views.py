from django.shortcuts import render

def graficas(request):
    # Datos para las seis gráficas
    context = {
        'data1': [10, 20, 30, 40],
        'labels1': ['monto 1', 'monto 2', 'monto 3', ' monto 4'],
        'data2': [15, 25, 35, 45],
        'labels2': ['mexico', 'canada', 'japon', 'China'],
        'data3': [5, 10, 15, 20],
        'labels3': ['bodega 1', 'bodega 2', 'bodega 3', 'bodega 4'],
        'data4': [8, 16, 24, 32],
        'labels4': ['cuatrimeste 1', 'cuatrimestre 2', 'cuatrimestre 3', 'cutrimestre 4'],
        'data5': [12, 14, 16, 18],
        'labels5': ['zona 1', 'zona 2', 'zona 3', 'zona 4'],
        'data6': [22, 28, 34, 40],
        'labels6': ['Samsung', 'iPhone de Apple', 'Xiaomi', 'Oppo'],
    }
    
    return render(request, 'graficas/graficas.html', context)
