var express = require('express');
var path = require('path');
var app = express();
var bodyParser = require('body-parser');


//configure app
// use middleware
// define route
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));//__dirname says the path the app.js resides in 
app.set('pyscript', path.join(__dirname, 'python_gen'));
//using the middleware
app.use(bodyParser());//can parse both josn and url encoded data
app.use(express.static(path.join(__dirname,'bower_components')));//tell express to serve files when a clients requests it
app.use(require('./todos'));
//routes - moved to todos.js
// app.get('/index', function(req, res){
//     //res.send('Hello Express ex');
//     //res.render('index',items = [{desc:'foo'}, {desc:'bar'}, {desc:'baz'}]);
//     res.render('index', {items: todoItems});
// });
// var todoItems = [
//     {id: 1, desc: 'foo'},
//     {id: 2, desc: 'bar'},
//     {id: 3, desc: 'challange'}
// ];

// app.get('/user:id', function(req, res){
//     //res.send(req.params.id);
//     //res.send(req.params);
//     //res.sendfile("abc.txt");
//     //res.send('<h1>'+req.params.id+'</h1>')
//     res.render('index', {items: todoItems});
// });

// app.post('/add', function(req,res){
//     var newItem = req.body.newItem;//so express needs body parser module to operate on the data in the views
//     //express needs modules to parse the values in the views 
//     console.log(newItem);
//     todoItems.push(
//         {id: todoItems.length + 1, desc: newItem});
//     res.redirect('/index')
// });

app.listen(1337,function(){
    console.log('listening on port 1337');
}); //the application will listen to this port


// var http = require('http');
// http.createServer(function (req,res){
// res.writeHead(200,{'Content-type': 'text/plain'});
// res.end('Hello World\n');
// }).listen(1337, '127.0.0.1');
// console.log('Server running at http://127.0.0.1:1337/')
