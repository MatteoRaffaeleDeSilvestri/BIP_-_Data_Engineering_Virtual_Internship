from time import time

if __name__ == '__main__':

    # Salary per age
    age_salary = {2: list(),
                  3: list(),
                  4: list(),
                  5: list()}

    # Salary per region
    region_salary = dict()

    skip = False

    try:
        
        # Import pandas module
        import pandas

        # Setting starting time
        s = time()
        
        # Reading .csv file
        print('\nStarting...')

        try:
            s_read = time()
            df = pandas.read_csv('Hr5m.csv', usecols = ['Age in Yrs.', 'Salary', 'Region'])
            e_read = time()
            print('Reading \'.csv\' file [{} sec.]'.format(round(e_read - s_read, 3)))
        
            # INDEX
            # 1: Age
            # 2: Salary
            # 3: Region

            # Analysing data from file
            s_iter = time()
            for item in df.itertuples():
                if int(item[1] // 10) == 6:
                    age_salary[int(item[1] // 10) - 1].append(item[2])
                else:    
                    age_salary[int(item[1] // 10)].append(item[2])
                if item[3] not in region_salary.keys():
                    region_salary.setdefault(item[3], [item[2]])
                else:
                    region_salary[item[3]].append(item[2])
            e_iter = time()
            print('Iterate through data [{} sec.]\n'.format(round(e_iter - s_iter, 3)))

        except FileNotFoundError:
            print('\nATTENTION: Hr5m.csv file not found.\n')
            skip = True

    except Exception as exception:
        
        # Print error
        print('\nATTENTION: {}. Check out the documentation for more information.'.format(exception))

        # Import csv module
        import csv
        
        # Setting starting time
        s = time()

        # Reading .csv file
        print('\nStarting...')

        try:
            s_read = time()
            with open('Hr5m.csv') as data:
                csv_data = csv.DictReader(data)
                e_read = time()
                print('Opening \'.csv\' file [{} sec.]'.format(round(e_read - s_read, 3)))   

                # Analysing data from file
                s_iter = time()
                for record in csv_data:
                    if int(float(record['Age in Yrs.']) // 10) == 6:
                        age_salary[int(float(record['Age in Yrs.']) // 10) - 1].append(float(record['Salary']))
                    else:    
                        age_salary[int(float(record['Age in Yrs.']) // 10)].append(float(record['Salary']))
                    if record['Region'] not in region_salary.keys():
                        region_salary.setdefault(record['Region'], [float(record['Salary'])])
                    else:
                        region_salary[record['Region']].append(float(record['Salary']))
                e_iter = time()
                print('Iterate through data [{} sec.]\n'.format(round(e_iter - s_iter, 3)))

        except FileNotFoundError:
            print('\nATTENTION: Hr5m.csv file not found.\n')
            skip = True

    if not skip:
        
        # Calculating salary per age
        print('CALCULATING AVERAGE SALARY PER AGE (upper limit excluded) (*)')
        s_calc_1 = time()
        for age in age_salary.keys():
            salary = str(round(sum(age_salary[age]) / len(age_salary[age]), 2))
            if len(salary[salary.index('.') + 1 : ]) < 2:
                salary += '0'
            print('{}-{}: {}'.format(age * 10, age * 10 + 10, salary))
        e_calc_1 = time()
        print('[{} sec.]\n'.format(round(e_calc_1 - s_calc_1, 3)))

        print('\n(*) In the age range 50-60 the upper limit of 60 years has been included in the calculation.')

        # Calculating salary per region
        print('CALCULATING AVERAGE SALARY PER REGION')
        s_calc_2 = time()
        for region in region_salary.keys():
            salary = str(round(sum(region_salary[region]) / len(region_salary[region]), 2))
            if len(salary[salary.index('.') + 1 : ]) < 2:
                salary += '0'
            print('{}: {}'.format(region, salary))
        e_calc_2 = time()
        print('[{} sec.]'.format(round(e_calc_2 - s_calc_2, 3)))

        e = time()
        print('\nOperation completed in {} sec.\n'.format(round(e - s, 3)))
