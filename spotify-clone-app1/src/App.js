import React, { useEffect, useState } from "react";
import './App.css';
import Login from "./Login";
import { getTokenFromUrl } from "./spotify";
import SpotifyWebApi from "spotify-web-api-js";
import Player from "./Player";
import { DataLayer, useDataLayerValue } from "./DataLayer";


const spotify = new SpotifyWebApi();


function App() {
  const [token, setToken] = useState(null);
  const [{ user }, dispatch] = useDataLayerValue();

  useEffect(() => {
    const hash = getTokenFromUrl();
    window.location.hash = "";

    const _token = hash.access_token;

    if (_token) {

      setToken(_token);

      dispatch()

      spotify.setAccessToken(_token); 

      spotify.getMe().then(user => {
        dispatch({
          type: "SET_USER",
          user: user,
        });
      });
    }
  
    console.log("I HAVE A TOKEN", token);
  // eslint-disable-next-line
  }, []);


  console.log("firstuser", user);


  return <div className="app">(token ? 
  <Player /> : 
  <Login />)
  </div>
}

export default App;
