import React, { useEffect, useState } from 'react';
import './ImageInfo.css'

const ImageInfo = (props) => {
    const [res, setRes] = useState(false)
    const getResult = () => {
        if (! props.ready) {
            return false
        }
        setRes(true)
        // get
    }
    return (
        <div className='image-info'>
            <img id='img_mammo' src={props.image}></img>
            <div className='analysis'>
                <button className={props.ready ? "" : "disabled"} onClick={() => getResult()}>Результат</button>
                {res && <div>тут должны быть результаты</div>}
            </div>
        </div>
    );
};

export default ImageInfo;