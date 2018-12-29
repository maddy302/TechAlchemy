var path = require('path');
var appRoot = path.resolve(__dirname);
var config = {
	web:{
		name:"TechAlchemy",
		appRoot:appRoot
	},
	url:{
		//host:"http://10.118.27.156:3000"
		host:"http://localhost:3000"
	},
	upload:{
		uploadPath:"",
		imageFloder:"/upload/images/",
		defaultAvatar:"/images/default-avatar.png"
	},
	auth:{
		activeKey : "activeKey",
		checkActive: false
	},
	database :{
		address : "mongodb://root:abc123@ds111082.mlab.com:11082/techalchemy"
	},
	session :{
		cookie : {
			secret: 'sessionSecret',
    		name: 'sessionName',
    		maxAge: 1000 * 60 * 60 * 24 * 30
		},
		database:{
        	address: 'mongodb://root:abc123@ds111082.mlab.com:11082/techalchemy'
		}
	},
	email:{
	    host: 'smtp.qq.com',
		port: 25,
		user: '123456789@qq.com',
		pass: '123456789',
		from: 'TechAlchemy<123456789@qq.com>'
	},
	topic:{
		page:{
			limit:10
		}
	}
};

module.exports = config;
