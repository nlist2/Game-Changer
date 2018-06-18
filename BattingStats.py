total = driver.find_element_by_tag_name('tfoot')
alltotals = total.find_element_by_class_name('totals.totals_all')
columns = alltotals.find_elements_by_tag_name('td')

with open('gc.csv', 'w') as f:
    csvwriter = csv.writer(f)
    headers = ['PA','AB','H', '1B', '2B', '3B', 'HR', 'RBI', 
'R', 'HBP', 'ROE', 'FC', 'CI', 'BB', 'K', 'AVG', 'OBP', 'SLG', 'OPS']
    csvwriter.writerow(headers)
    for row in allRows:
        PA = columns[1].text
        AB = columns[1].text
        H = columns[2].text
        1B = columns[3].text
        2B = columns[4].text
        3B = columns[5].text
        HR = columns[6].text
        RBI = columns[7].text
        R = columns[8].text
        HBP = columns[9].text
        ROE = columns[10].text
        FC = columns[11].text
        CI = columns[12].text
        BB = columns[13].text
        K = columns[14].text
        AVG = columns[15].text
        OBP = columns[16].text
        SLG = columns[17].text
        OPS = columns[18].text
        tempList = [PA, AB, H, 1B, 2B, 3B, HR, RBI, R, HBP, ROE, FC, CI, BB, K, AVG, OBP, SLG, OPS]
        csvwriter.writerow(tempList)