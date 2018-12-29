var express = require('express');

var router = express.Router();
var todoItems = [
    {id: 1, desc: 'foo'},
    {id: 2, desc: 'bar'},
    {id: 3, desc: 'challange'}
];
var interest_w = '';
var skill_w = '';
var idea_results = '';
var idea_list ;

router.get('/index', function(req, res){
    //res.send('Hello Express ex');
    //res.render('index',items = [{desc:'foo'}, {desc:'bar'}, {desc:'baz'}]);
    console.log('Testing');
    console.log(__dirname);
    //console.log(pyscript);
    //idea_list = idea_results.split('||');
    res.render('index', {items: todoItems,interest_x:interest_w,skill_x:skill_w,idea_results:idea_results,idea_list:idea_list});
});


router.get('/user:id', function(req, res){
    //res.send(req.params.id);
    //res.send(req.params);
    //res.sendfile("abc.txt");
    //res.send('<h1>'+req.params.id+'</h1>')
    res.render('index', {items: todoItems});
});

router.post('/add', function(req,res){
    var newItem = req.body.newItem;//so express needs body parser module to operate on the data in the views
    //express needs modules to parse the values in the views 
    interest_w = req.body.interests;
    skill_w = req.body.skill;
    console.log(newItem);
    // const spawn = require("child_process").spawn;
    // var arg1 = "3";
    // var arg2 = "4";
    // //console.log(typeof(arg1))
    // const pythonProcess = spawn('python',[__dirname+"python_gen/test_hello.py",arg1,arg2]);
    // data = [1,2],
    // dataString = '';
    // pythonProcess.stdout.on('data',(data)=>{
    //     console.log(typeof(data));
    //     console.log(data);
    // })
    // pythonProcess.stdout.on('end', function(){
    //     console.log('python program ended');
    //   });
    // pythonProcess.stdin.write(JSON.stringify(data));
    // pythonProcess.stdin.end();

    program_path = __dirname+'/python_gen/';
    var PythonShell = require('python-shell');
    var options = {
        mode: 'text',
        pythonPath: 'C:/Users/Madhukar/Anaconda2/python.exe',
        pythonOptions: ['-u'],
        scriptPath: program_path,
        //args: ['1', '5']
        //args: [program_path, '1', '5']
        args: [program_path, interest_w, skill_w]
      };
      PythonShell.run('test.py', options, function (err, results) {
        if (err) throw err;
        // results is an array consisting of messages collected during execution
        console.log('results: %j', results);
        idea_results = results;
      });
    todoItems.push(
        {id: todoItems.length + 1, desc: newItem, skill_w: skill_w, interest_w:interest_w });
    console.log(skill_w,)
    res.redirect('/index');
});

module.exports = router;