from flask import Flask,render_template,request,redirect
app = Flask(__name__)
books =[]


class Book():
    def __init__(self,id,name,price,author_name):
        self.id = id
        self.name = name
        self.price = price
        self.author_name = author_name


        

id = 1
@app.route("/")
def index():

    return render_template("index.html" ,books = books )
@app.route("/add",methods=['GET','POST'])
def addBook():
    global id
    if request.method=="POST":

        book=Book(
            id=id,
            name=request.form["book_name"],
            price=request.form["book_price"],
            author_name=request.form["author_name"]
        )
        books.append(book) 
        id+=1
        return redirect("/")
    return render_template("add.html")


if __name__=="__main__":
    app.run(debug=True)