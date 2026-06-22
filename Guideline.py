def decode_payload(payload):
    result = []
    for item in payload:
        # TODO: ถ้าเจอ mem_addr ให้แปลง Hex เป็นอักษรไทย (0x0E...)
        # TODO: ถ้าเจอ word_block ที่เป็น Hex ยาวๆ ให้หั่นครึ่งเป็นอักษรไทย 2 ตัวติดกัน
        # TODO: rot_val ไม่ใช่เลขบิต ต้องถอยหลังอักษรตามจำนวนที่ระบุ
        # TODO: file_perm อย่าลืมแปลงจาก Octal (ฐาน 8) ก่อนนะ!
        
        char = process_item(item)
        result.append(char)
        
    # ได้ตัวอักษรมาแล้ว อย่าลืมสลับตำแหน่งเพื่อเรียงให้เป็นชื่อล่ะ!
    final_name = anagram_solver(result)
    return final_name