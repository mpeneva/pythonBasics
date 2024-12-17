
processor_price = float(input()) * 1.57
video_card_price = float(input()) * 1.57
ram_memory_price = float(input()) * 1.57
ram_memory_count = int(input())
discount = float(input())

#1 usd = 1.57 лева.

total_memory_price = ram_memory_count * ram_memory_price

video = video_card_price - video_card_price * discount
processor_dc = processor_price - processor_price * discount

video_processor = video + processor_dc


total_pc = total_memory_price + video_processor

print(f"Money needed - {total_pc:.2f} leva.")