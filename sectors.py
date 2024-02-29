domain = 'http://www.moneycontrol.com/stocks/sectors'
sectors_url = {
    'pharma' : f'{domain}pharmaceuticals.html',
    'chem' : f'{domain}/chemicals.html',
    'cs' : f'{domain}/computers-software.html',
    'fert' : f'{domain}/fertilisers.html',
    'petrochem' : f'{domain}/petrochemicals.html',
    'trading' : f'{domain}/trading.html',
    'cement' : [f'{domain}/cement-major.html', f'{domain}/cement-mini.html'],
    'banks' : [f'{domain}/banks-private-sector.html', f'{domain}/banks-public-sector.html'],
    'finance' : [f'{domain}/finance-general.html',f'{domain}/finance-housing.html',f'{domain}/finance-investments.html',f'{domain}/finance-leasing-hire-purchase.html',f'{domain}/finance-term-lending-institutions.html'],
    'steel' : [f'{domain}/steel-large.html', f'{domain}/steel-medium-small.html'],
    'misc' : f'{domain}/miscellaneous.html'
}