def number_to_text_convert(number):
    n = int(number)
    highers = ['Lakh Crores', 'Lakh Crore', 'Hundred Cores', 'Hundred Core', 'Cores', 'Core', 'Lakhs', 'Lakh',
             'Thousands', 'Thousand', 'Hundred', 'Hundred']
    tens = [' ', ' ', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    units = [" ", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Eleven", "Twelve",
           "Thirteen",
           "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

    lakhCrores = (n // 100000000000) % 100
    hundredCrores = (n // 1000000000) % 100
    crore = (n // 10000000) % 100
    lakh = ((n // 100000) % 100)
    thousand = ((n // 1000) % 100)
    hundred = ((n // 100) % 10)
    rest = (n % 100)
    finalWord = ""

    if (lakhCrores > 0):
       if (lakhCrores > 9 and lakhCrores <= 19):
            finalWord = finalWord + " " + units[lakhCrores] + " " + highers[0]
       elif (lakhCrores > 19):
            finalWord = finalWord + " " + tens[lakhCrores // 10] + " " + units[lakhCrores % 10] + " " + highers[
                 0]
       else:
            finalWord = finalWord + " " + units[lakhCrores] + " " + highers[1]

    if (hundredCrores > 0):
       if (hundredCrores > 9 and hundredCrores <= 19):
            finalWord = finalWord + " " + units[hundredCrores] + " " + highers[2]
       elif (hundredCrores > 19):
            finalWord = finalWord + " " + tens[hundredCrores // 10] + " " + units[hundredCrores % 10] + " " + \
                        highers[2]
       else:
            finalWord = finalWord + " " + units[hundredCrores] + " " + highers[3]

    if (crore > 0):
       if (crore > 9 and crore <= 19):
            finalWord = finalWord + " " + units[crore] + " " + highers[4]
       elif (crore > 19):
            finalWord = finalWord + " " + tens[crore // 10] + " " + units[crore % 10] + " " + highers[4]
       else:
            finalWord = finalWord + " " + units[crore] + " " + highers[5]

    if (lakh > 0):
       if (lakh > 9 and lakh <= 19):
            finalWord = finalWord + " " + units[lakh] + " " + highers[6]
       elif (lakh > 19):
            finalWord = finalWord + " " + tens[lakh // 10] + " " + units[lakh % 10] + " " + highers[6]
       else:
            finalWord = finalWord + " " + units[lakh % 10] + " " + highers[7]

    if (thousand > 0):
       if (thousand > 9 and thousand < 20):
            finalWord = finalWord + " " + units[thousand] + " " + highers[8]
       elif (thousand > 19):
            finalWord = finalWord + " " + tens[thousand // 10] + " " + units[thousand % 10] + " " + highers[8]
       else:
            finalWord = finalWord + " " + units[thousand % 10] + " " + highers[9]

    if (hundred > 0):
       if ((hundred // 100)):
            finalWord = finalWord + " " + units[hundred % 10] + " " + highers[10]
       else:
            finalWord = finalWord + " " + units[hundred % 10] + " " + highers[11]

    if (rest > 19):
       finalWord = finalWord + " " + tens[rest // 10] + " " + units[rest % 10]

    else:
       finalWord = finalWord + units[rest]

    if (n == 0):
       finalWord = "Zero"

    return finalWord + " Taka Only."
    
if __name__ == "__main__":
    digit = 125000
    print(number_to_text_convert(digit))
