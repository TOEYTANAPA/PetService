var events = {
	// '11-21-2016' : [{content: 'Great American Smokeout', url: 'http://www.wincalendar.com/Great-American-Smokeout', allDay: true}],
	// '11-11-2016' : [{content: 'Remembrance Day (Canada)', url: 'http://www.wincalendar.com/Remembrance-Day', allDay: true}], 
	// '04-01-2016' : [{content: 'Start Skagit Valley Tulip Festival ', repeat: 'MON', allDay: true, endDate: '04-30-2100'}],
	// '12-25-2016' : [{content: 'Christmas Day', repeat: 'FRI', allDay: true, endDate: '12-25-2100'}],
	// '01-01-2016' : [{content: 'New Year\'s', repeat: 'THU', allDay: true, endDate: '12-31-2100'}],
	// '01-01-2016' : [{content: 'Yeah Monthly', repeat: 'WED', allDay: true, endDate: '07-02-2100'}],
	// '01-07-2016' : [{content: 'Dummy Text', repeat: 'TUE', allDay: true, endDate: '02-07-2100'}],
	// '01-15-2016' : [{content: 'Lorem Ipsum was popularised', repeat: 'WED', allDay: true, endDate: '02-07-2100'}],
	// '03-02-2016' : [{content : 'Graduation Exams', repeat: 'SUN', allDay: true, endDate: '03-20-2100'}],
	'01-01-2016' : [{content : 'MONDAY (WEEKLY)', repeat: 'MON', allDay: true, endDate:'01-01-2100'}]
	// '01-02-2016' : [{content : 'TUESDAY (WEEKLY)', repeat: 'TUE', allDay: true, endDate:'01-02-2100'}]
	// '01-03-2016' : [{content : 'Wednesday (WEEKLY)', repeat: 'WED', allDay: true, endDate:'01-03-2100'}]
	// '01-04-2016' : [{content : 'Thursday (WEEKLY)', repeat: 'THU', allDay: true, endDate:'01-04-2100'}]
	// '01-05-2016' : [{content : 'Saturday (WEEKLY)', repeat: 'FRI', allDay: true, endDate:'01-05-2100'}]
	// '01-06-2016' : [{content : 'Friday (WEEKLY)', repeat: 'SAT', allDay: true, endDate:'01-06-2100'}]
	// '01-07-2016' : [{content : 'Sunday (WEEKLY)', repeat: 'SUN', allDay: true, endDate:'01-07-2100'}]
},



t = new Date(),
//Creation of today event
today = ((t.getMonth() + 1) < 10 ? '0' + (t.getMonth() + 1) : (t.getMonth() + 1)) + '-' + (t.getDate() < 10 ? '0' + t.getDate() : t.getDate()) + '-' +t.getFullYear();
events[today] = [{content: 'TODAY', allDay: true}];
