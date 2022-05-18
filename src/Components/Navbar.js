import React, { useState } from 'react';
import './Navbar.css'

const Navbar = (props) => {
    const clickInput = () => {
        const input = document.querySelector('#file-upload');
        input.click();
    }

    const postFile = () =>  {
        let f = document.querySelector('#file-upload').files[0];
        if (f) {
            const imgSrc = URL.createObjectURL(f);
            props.updateImg(imgSrc);
            if (props.readySystem) {
                props.updateReady()
            }
            //post-method
        }
        
    }

    return (
        <div className="navbar">
            <span className="main-text">система анализа маммограмм</span>
            <div className='buttons'>
                <div className='upload-container'>
                    <input id="file-upload" type="file" name='f' accept='image/jpeg, image/png' onChange={postFile}></input>
                    <div className='btn-upload' onClick={clickInput}>Загрузить файл
                    </div>
                </div>
                {/* <button></button> */}
                <button>Инфо</button>
            </div>
            <span className='project-of'><p>Проект</p>Наталии Сенаторовой & Ксении Гук</span>
        </div>
    );
};

export default Navbar;