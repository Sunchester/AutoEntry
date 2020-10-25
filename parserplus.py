def parse_Text(file):
    output_list = []
    fileOpen = open(file, 'r')
    line = fileOpen.readline()
    while line:
        line = line.strip()
        output_list.append(line)
        line = fileOpen.readline()
    fileOpen.close()
    return output_list

def verify_Eligibility(title):
    if 'Already Played' in title:
        return False
    else:
        return True

def check_Winner(title):
    if 'Congratualtions' in title:
        return True
    else:
        return False
