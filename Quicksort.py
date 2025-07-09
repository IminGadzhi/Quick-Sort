# Test commit file
# Bước 1: Tạo mảng chứa danh sách các số nguyên nhập vào

# Yêu cầu người dùng nhập một chuỗi các số, cách nhau bằng dấu cách
input_str = input("Nhập dãy số nguyên, cách nhau bằng dấu cách: ")

# Tách chuỗi thành các phần tử, rồi chuyển từng phần tử thành số nguyên
numbers = list(map(int, input_str.strip().split()))

# In ra mảng đã nhập để kiểm tra
print("Dãy số đã nhập:", numbers)
# Hàm quicksort sắp xếp danh sách theo thứ tự tăng dần
def quicksort(arr):
    if len(arr) <= 1:
        return arr  # Mảng rỗng hoặc 1 phần tử thì đã được s(ắp sẵn rồi

    pivot = arr[0]  # Chọn phần tử đầu tiên làm pivot
    less = [x for x in arr[1:] if x <= pivot]  # Nhỏ hơn hoặc bằng pivot
    greater = [x for x in arr[1:] if x > pivot]  # Lớn hơn pivot

    return quicksort(less) + [pivot] + quicksort(greater)
print("Dãy số đã sắp xếp:", quicksort(numbers))
