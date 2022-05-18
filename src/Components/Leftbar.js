import React, { useState } from 'react';
import './Leftbar.css'

const Leftbar = (props) => {
    const [system, setSystem] = useState(undefined)
    const [classifier, setClassifier] = useState(undefined)
    const [systemChosen, setSystemChosen] = useState(false)
    const classifiers = ['Support Vector Machine', 'Decision Tree', 'K-Nearest Neighbors', 'Linear Discriminant Analysis', 'Ada Boost','Random Forest', 'Multi-layer Perceptron']
    const img = props.img
    const chooseSystem = (num) => {
        setSystemChosen(true);
        setSystem(num)
    }
    
    const chooseClassifier = (id) => {
        setClassifier(id);
        if (props.readyImg) {
            props.updateReady()
        }
        props.updateReadySystem()
    }

    const renderClassifers = () => {
        const system1 = <div style={{display: 'flex', flexDirection: 'row'}}>
            <button className="classifier-btn" onClick={() => chooseClassifier(1)}>SVM</button>
            <button className="classifier-btn" onClick={() => chooseClassifier(2)}>DT</button>
            <button className="classifier-btn" onClick={() => chooseClassifier(3)}>KNN</button>
            <button className="classifier-btn" onClick={() => chooseClassifier(4)}>LDA</button>
        </div>
        const system2 = <div style={{display: 'flex', flexDirection: 'row'}}>
        <button className="classifier-btn" onClick={() => chooseClassifier(5)}>AB</button>
        <button className="classifier-btn" onClick={() => chooseClassifier(6)}>RF</button>
        <button className="classifier-btn" onClick={() => chooseClassifier(1)}>SVM</button>
        <button className="classifier-btn" onClick={() => chooseClassifier(7)}>MLP</button>
        <button className="classifier-btn" onClick={() => chooseClassifier(3)}>KNN</button>
    </div>
    return system === 1? system1 : system2
    }

    return (
        <div className='leftbar'>
            <div className='system'>
                <label className='choose-system'>
                    <img src='./ico.png'  alt='' height={15} style={{marginRight: '5px', marginBottom: '-2px'}}/>
                    выбрать систему
                    </label>
                <button onClick={() => chooseSystem(1)}>1</button>
                <button onClick={() => chooseSystem(2)}>2</button>
            </div>
            {systemChosen && <div className='methods'>
                <label className='about-system'>
                {system === 1 ? <p className='about'>описание первой системы</p> : <p className='about'>описание второй системы</p>}
                </label>
            </div>}
            {systemChosen && <div className='classifier'>
            <label className='choose-system'>
                    <img src='./ico.png'  alt='' height={15} style={{marginRight: '5px', marginBottom: '-2px'}}/>
                    выбрать классификатор
                    </label>
                    {renderClassifers()}
                    {classifier && <label className='chosen-cl'>выбранный классификатор: {classifiers[classifier - 1]}</label>}
            </div>}
        </div>
    );
};

export default Leftbar;