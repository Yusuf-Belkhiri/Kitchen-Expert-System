from flask import Flask, render_template, request , session , redirect
from programm_core import forwardChainQuery


app = Flask(__name__)
app.secret_key = "dposajdposajdposajdpo"



@app.route('/',methods = ['GET'])
def MainPage():
    session.pop('dish',default=None)
    session['result'] = []
    result = session['result']
    #result = ['asd','asd']
    print('sadsadsadsad')
    return render_template('/Html/index.html',result=result)




@app.route('/Second.html',methods = ['GET'])
def SecondPage():

    print('sadsadsadsad')
    return render_template('/Html/Second.html')

def convert(req):
    try :
        return int(req)

    except:
        return 0


@app.route('/Second.html',methods = ['POST'])
def res1():
    result = []
    input_data = {

    }
    try:
        print('dsadsad')
        dish = session['dish']
        print('the dish setter works fine')
    except :
        dish = ""

    params = []

    ingredients = request.form.getlist('ingredient')
    print('i am here')
    for ingredient in ingredients :
        temp= max(1000,convert(request.form.get(ingredient+"Quantity")))
        if temp <= 100 :
            input_data[ingredient] = "Few"
        elif temp <= 500 :
            input_data[ingredient] = "Med"
        else :
            input_data[ingredient] = "Much"

    
    tools = request.form.getlist('tool')

    for key,value in input_data.items():
        params.append(f"HaveIngredient({key}, {value})")

    for tool in tools :
        params.append(f"HaveTool({tool})")

    result = forwardChainQuery(params)

    if dish != "" and dish is not None: 
        
        if dish not in result :
            result  = ['Sorry But You Can NOT Cook This Particulair Dish With What You Have ']
        else :
            result = []
            result.append('You Can Make This Dish With the Ingredients And Tools You Have! Bonne Apetit!!!')

    if(len(result) == 0 and not dish): result = ['Sorry But There Is Nothing You Can Cook With These Ingredients/    ']
    #print(input_data)
    session['result'] = result
    session['dish'] = ""
    return redirect('/result.html')


@app.route('/Third.html',methods = ['GET'])
def res2():

    print('sadsadsadsad')
    return render_template('/Html/Third.html')


@app.route('/Third.html',methods = ['POST'])
def res22():
    session['dish'] = request.form.get('dishSelect')
    print('This is what happens')
    print(session['dish'])
    print('This is what happens')
    return redirect('/Second.html')


@app.route('/result.html',methods = ['GET'])
def res3():

    result = session['result']
    session['dish'] = ""
    session['result'] = []
    print('sadsadsadsad')
    return render_template('/Html/result.html',result = result)


if __name__ == "__main__":
    app.run(port=8080)
