import React from 'react'
import './Login.css';
import { loginUrl } from './spotify';

//creating login page
function Login() {
    return (
        <div className="Login">
        {/* Spotify Clone Logo */}
        <img
            src="https://www.freepnglogos.com/uploads/spotify-logo-png/spotify-icon-marilyn-scott-0.png" width="200" 
            alt=""
        />

        {/* Login button */}
        <a href ={loginUrl}>LOGIN WITH SPOTIFY</a>
        </div>
    );
}


export default Login;

