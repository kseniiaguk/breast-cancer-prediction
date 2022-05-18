import React, { useState } from 'react';
import Navbar from './Components/Navbar';
import './App.css'
import Leftbar from './Components/Leftbar';
import ImageInfo from './Components/ImageInfo';

const App = () => {
    const [img, setImg] = useState(undefined)
    const [ready, setReady] = useState(false)
    const [readySystem, setReadySystem] = useState(false)
    const [readyImg, setReadyImg] = useState(false)
    const updateImg = (val) => {
        setImg(val);
        setReadyImg(true)
    }

    const updateReady = () => {
        setReady(true)
    }

    const updateReadySystem = () => {
        setReadySystem(true)
    }

    return (
        <div>
            <Navbar updateImg={updateImg} updateReady={updateReady} readySystem={readySystem}></Navbar>
            <div className='central-part'>
                <Leftbar updateReady={updateReady} readyImg={readyImg} updateReadySystem={updateReadySystem}></Leftbar>
                <ImageInfo image={img} ready={ready}></ImageInfo>
            </div>
        </div>
    );
};

export default App;