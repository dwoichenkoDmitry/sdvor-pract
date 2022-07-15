import React, {useEffect, useRef} from 'react';
import classes from './Popup.module.css'
import axios from "axios";

const Popup = ({list, vision, setVision}) => {
    function useOutsideAlerter(ref) {
        useEffect(() => {
            /**
             * Alert if clicked on outside of element
             */
            function handleClickOutside(event) {
                if (ref.current && !ref.current.contains(event.target)) {
                    setVision(false)
                }
            }

            // Bind the event listener
            document.addEventListener("mousedown", handleClickOutside);
            return () => {

                document.removeEventListener("mousedown", handleClickOutside);
            };
        }, [ref]);
    }

    const wrapperRef = useRef(null);
    useOutsideAlerter(wrapperRef);

    function ShowImage(path){
        console.log("http://127.0.0.1:8000/img/"+path)
    }

    return (
        <div>


        {vision?
    <div ref={wrapperRef} className={classes.container}>
        <div className={classes.row}>
            <h3>Номер</h3>
            <h3>Баркод</h3>
            <h3>Тип штихкода</h3>
        </div>
        <div className={classes.line}/>
        {list.map((item, index)=>
            <div onClick={(e)=> {ShowImage(item.name)}} key={index} className={classes.row}>
                <h4>{item.number}</h4>
                <h4>{item.barcode}</h4>
                <h4>{item.type}</h4>
            </div>
        )}
    </div>
                :
                ''
}
        </div>
    );
};

export default Popup;