def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Diziyi ikiye böl
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Recursive olarak sol ve sağ parçaları sırala
    left = merge_sort(left)
    right = merge_sort(right)
    
    # Sıralı parçaları birleştir
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    # İki sıralı diziyi karşılaştırarak birleştir
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Kalan elemanları ekle
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

def print_steps(arr, depth=0):
    indent = "  " * depth
    print(f"{indent}Böl: {arr}")
    
    if len(arr) <= 1:
        print(f"{indent}Sonuç: {arr}")
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    print(f"{indent}Sol: {left}, Sağ: {right}")
    
    left_sorted = print_steps(left, depth + 1)
    right_sorted = print_steps(right, depth + 1)
    
    merged = merge(left_sorted, right_sorted)
    print(f"{indent}Birleştir: {merged}")
    
    return merged

if __name__ == "__main__":
    arr = [16, 21, 11, 8, 12, 22]
    print("=== MERGE SORT AŞAMALARI ===")
    print(f"Orijinal dizi: {arr}")
    print("\n--- Adım Adım İşlem ---")
    sorted_arr = print_steps(arr)
    print(f"\nSon sonuç: {sorted_arr}")
    
    print("\n=== BIG-O KARMAŞIKLIĞI ===")
    print("Zaman Karmaşıklığı: O(n log n)")
    print("Yer Karmaşıklığı: O(n)")