a = 4
b = 5
print("--- ANTES ---")
print(f"A vale: {a}")
print(f"B vale: {b}")
a, b = b, a
print("\n--- DESPUÉS ---")
print(f"A vale: {a}")
print(f"B vale: {b}")