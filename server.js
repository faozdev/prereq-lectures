const { spawn } = require('child_process');
const {PythonShell} = require('python-shell');
var createError = require('http-errors');
const express = require('express');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
var path = require('path');


const app = express();
const port = 3000;



app.get('/', (req, res) => {
    const pythonProcess = spawn('python', ['main.py']);

    pythonProcess.on('close', (code) => {
      console.log(`Python process is over, exit code: ${code}`);
    });
    res.sendFile(__dirname +'/index.html');

    
});

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.listen(port, () => {
    console.log(`Server works in http://localhost:${port}`);
});

app.post('/curriculum', (req, res) => {
    res.setHeader('Content-Type', 'application/json');
    res.status(200).json({ message: 'Başarılı JSON yanıtı' });
    var iterationFormValue = req.body.iterationFormValue;
    console.log(iterationFormValue);
    const python2Process = spawn('python', ['curriculum.py', iterationFormValue]);
    let dataString = {
        ScriptPath: __dirname + '/curriculum.py',
        args: [iterationFormValue]
    };
    PythonShell.run(dataString.ScriptPath, {args: dataString.args}, function(err, results) {
        if (err) throw err;
        console.log(results);
    });
});

