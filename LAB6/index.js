const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const fs = require('fs');
const ejs = require('ejs');
const sqlite3 = require('sqlite3');
const sqlite = require('sqlite');

app.set('view engine', 'ejs');
app.use(express.static(__dirname + '/public'));

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: false}));

async function getDBConnection() {
    const db = await sqlite.open( {
        filename: 'product.db',
        driver: sqlite3.Database
    });
    return db;
}

let prods = [];
getData();

async function getData() {
    let db = await getDBConnection();
    let rows = await db.all('SELECT * FROM product');
    await db.close();
    for (let i=0; i<rows.length; i++) {
        let prodObject = {
            pro_id : rows[i]['product_id'],
            pro_title : rows[i]['product_title'],
            pro_price : rows[i]['product_price'],
            pro_img : rows[i]['product_image'],
            pro_cate : rows[i]['product_category']
        }
        prods.push(prodObject);
    }
    return prods;
}

app.get('/', async function(req, res){
    res.render('index', {
        products: prods
    });
});

//Writing Comments File I/O
let readdata = fs.readFileSync('comments.json');
let allComments = JSON.parse(readdata);
var ProductReview = {};
ProductReview.reviewArray = allComments.reviewArray;

app.get("/product/:id", (req, res) => {
    console.log(ProductReview.reviewArray);
    res.render('template', {
        product : prods[req.params.id-1],
        review : ProductReview.reviewArray
    });
});

app.post("/addComment/:id", (req, res) => {
    ProductReview.reviewArray.push({product_id: req.params.id, comment: req.body.newcomment});
    var forJson = JSON.stringify(ProductReview); 
    fs.writeFileSync('comments.json', forJson);
});

//Filtering Products
app.post("/search", (req, res) => {
    var category = req.body.searchct;
    var keyword = req.body.searchkw;
    res.render('index', {
        products: filter(category, keyword)
    });
});

function filter(category, keyword) {
    let filtered = [];
    if (category == "All") {
        category = undefined;
    }
    if (category != undefined && keyword == undefined) {
        prods.forEach((pro) => {
            if(pro.pro_cate == category) {
                filtered.push(pro);
            }
        });
    } else if (category == undefined && keyword != undefined) {
        prods.forEach((pro) => {
            if(pro.pro_title.toUpperCase().indexOf(keyword.toUpperCase()) != -1) {
                filtered.push(pro);
            }
        });
    } else if (category != undefined && keyword != undefined) {
        prods.forEach((pro) => {
            if(pro.pro_title.toUpperCase().indexOf(keyword.toUpperCase()) != -1 && pro.pro_cate == category) {
                filtered.push(pro);
            }
        });
    } else {
        return prods;
    } return filtered;
}

app.get("/login", (req, res) => {
    res.render('login')
});
app.get("/signup", (req, res) => {
    res.render('signup')
});

const PORT = 3000;

app.listen(PORT, () => {
    console.log("서버가 실행됐습니다.");
    console.log(`서버주소: http://localhost:${PORT}`);
});