#purchase_data['DateTime'] = purchase_data.to_datetime(df['date'])
purchase_data['Year']=[d.split('/')[2] for d in purchase_data.date]
purchase_data['Month']=[d.split('/')[1] for d in purchase_data.date]
purchase_data['Day']=[d.split('/')[0] for d in purchase_data.date]
purchase_data.Year = purchase_data.Year.astype('int')
purchase_data.Month = purchase_data.Month.astype('int')
purchase_data.Day = purchase_data.Day.astype('int')
purchase_data.drop(['date'], axis = 1, inplace= True)
