
# Create string with 'Facebook'
# Create counter variable
# Check if input is empty, return
# iterate over characters of given word
# if char in given word == char in facebook, add counter
# if len == facebook, true, else: false  

def fbInString(input):
    fb = "facebook"
    counter = 0

    if not input:
        return False

    for i in range(len(input)):
        if input[i] == fb[counter]:
            counter += 1
        
        if counter == len(fb):
            return True
    
    return False

if __name__ == '__main__':
    print(fbInString("ffffaaccccebbok"))
    print(fbInString("is instagram owned by facebook?"))
    print(fbInString("ffffaacccebbooook"))
    print(fbInString(""))
