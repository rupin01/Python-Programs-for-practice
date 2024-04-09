def num_layers(n):
    initial_thickness_mm=0.5
    final_thickness_mm=initial_thickness_mm*(2**n)
    final_thickness_m=final_thickness_mm/1000
    return f"{final_thickness_m:.3f}m"
print(num_layers(1))
print(num_layers(4))
print(num_layers(21))