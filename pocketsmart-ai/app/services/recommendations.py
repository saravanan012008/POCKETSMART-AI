from urllib.parse import quote_plus

def marketplace_link(platform, query):
    q = quote_plus(query)
    urls = {
        'Amazon': f'https://www.amazon.in/s?k={q}',
        'IKEA': f'https://www.ikea.com/in/en/search/?q={q}',
        'Flipkart': f'https://www.flipkart.com/search?q={q}',
        'Swiggy': f'https://www.swiggy.com/search?query={q}',
        'Zomato': f'https://www.zomato.com/search?query={q}',
        'OYO': f'https://www.oyorooms.com/search?location={q}',
    }
    return urls.get(platform, f'https://www.google.com/search?q={q}')

def demo_home(data):
    b = data['budget']; allocations = {'Furniture': round(b*.35,2), 'Lighting': round(b*.18,2), 'Decor': round(b*.22,2), 'Utility': round(b*.15,2), 'Buffer': round(b*.10,2)}
    base = [('Furniture','Compact dining table','IKEA',allocations['Furniture']*.65,'Good fit for a practical, style-led setup.'),('Lighting','Warm LED lighting set','Amazon',allocations['Lighting']*.45,'Balances ambience and value.'),('Decor','Minimal wall art set','Flipkart',allocations['Decor']*.25,'Adds personality without consuming the budget.'),('Utility','Ceiling fan with energy-saving motor','Amazon',allocations['Utility']*.75,'Functional priority with room for savings.')]
    return _result('home', b, allocations, base, ['Keep the 10% buffer for delivery or installation.','Compare final prices and availability before purchase.'])

def demo_party(data):
    b=data['budget']; allocations={'Catering':round(b*.50,2),'Venue':round(b*.20,2),'Decoration':round(b*.15,2),'Entertainment':round(b*.10,2),'Buffer':round(b*.05,2)}
    base=[('Catering',f'{data["food_preference"]} catering package','Zomato',allocations['Catering'],'Flexible menu choices for the guest count.'),('Venue',f'{data["venue"]} venue shortlist','OYO',allocations['Venue'],'Useful for comparing stay/venue-style options.'),('Decoration','Theme decoration package','Amazon',allocations['Decoration'],'Simple decor components can reduce setup costs.'),('Entertainment','Party games / speaker setup','Flipkart',allocations['Entertainment'],'Keeps entertainment within a controlled allocation.')]
    return _result('party', b, allocations, base, ['Confirm per-person food pricing.','Keep a buffer for last-minute guest changes.'])

def demo_jewelry(data):
    b=data['budget']; allocations={'Primary jewelry':round(b*.65,2),'Secondary piece':round(b*.20,2),'Buffer':round(b*.15,2)}
    base=[('Necklace','Elegant statement necklace','Amazon',allocations['Primary jewelry'],'Works as a focal piece for the selected occasion.'),('Earrings','Coordinated drop earrings','Flipkart',allocations['Secondary piece'],'Adds balance without exceeding the planned spend.')]
    return _result('jewelry', b, allocations, base, ['Match metal tone with the outfit accessories.','Use the buffer for taxes, delivery, or a matching add-on.'])

def _result(planner,budget,allocations,items,tips):
    recs=[{'category':c,'title':t,'platform':p,'estimated_price':round(price,2),'reason':r,'link':marketplace_link(p,t)} for c,t,p,price,r in items]
    return {'planner':planner,'budget':budget,'summary':f'Demo plan created for a ₹{budget:,.0f} budget. Add a Gemini API key for live AI-generated recommendations.','allocations':allocations,'recommendations':recs,'tips':tips,'demo_mode':True}
