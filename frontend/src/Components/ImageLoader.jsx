import React, {useState} from 'react';
import classes from "./ImageLoader.module.css";
import axios from "axios";
import Popup from "./Popup";

const ImageLoader = () => {
    const [images, setImages] = useState('')
    const [image, setImage] = useState('')
    const [values, setVslues] = useState({number: '', barcode: '', type: ''})
    const [valList, setList] = useState([])
    const [vision, setVision] = useState(false)
    function ChangeLink(e) {
        setImages(URL.createObjectURL(e.target.files[0]))
        setImage(e.target.files[0])
    }

    async function GetImg() {
        let url = 'http://localhost:8000/getImg/'
        setList([])

        await axios.get(url
        ).then(request => {
            for(let i=0; i<request.data.number.length; i++){
                valList.push({number: request.data.number[i],
                    barcode: request.data.barcode[i], type: request.data.type[i], name: request.data.path[i]})
                setList(valList)
            }
            console.log(valList)
        })
            .catch(err => console.log(err))
        setVision(true)
    }

    async function SendImg() {
        if (image!==''){
            const formData = new FormData()
            formData.append('photo', image)
            formData.append('name', image.name)
            let url = 'http://localhost:8000/loadImg/'

            await axios.post(url, formData,
                {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                }
                ).then(request => {
                console.log(request)
                    setVslues({number: request.data.number, barcode: request.data.barcode, type: request.data.type})
            })
                .catch(err => console.log(err))
        }
    }

    function prob(){
        setVslues({number: '6584950678'})
    }

    return (
        <div className={[classes.container,classes.centered, values.number===''?'':classes.animFirst].join(' ')}>
            {/*<div className={classes.leftSide}>*/}
            {/*    <input className={classes.loaderInput} type="file" accept="image/*" onChange={ChangeLink}/>*/}
            {/*    <button className={classes.sendBtn} onClick={SendImg}>Отправить</button>*/}

            {/*    {values.number !== '' ?*/}
            {/*        <div>*/}
            {/*            <h2>number: {values.number}</h2>*/}
            {/*            <h2>barcode: {values.barcode}</h2>*/}
            {/*            <h2>type: {values.type}</h2>*/}
            {/*        </div>*/}

            {/*        :*/}
            {/*        ''*/}

            {/*    }*/}
            {/*</div>*/}
            {/*<div className={classes.rightSide}>*/}
            {/*    <img className={classes.loadImg} src={images}/>*/}
            {/*</div>*/}

            <div className={[classes.buttons, values.number===''?classes.cent:''].join(' ')}>
                <button onClick={GetImg} className={classes.mainBut}>лупа</button>
                <button onClick={SendImg} className={classes.mainBut} >Отправить</button>
            </div>
            <input className={classes.loaderInput} type="file" accept="image/*" onChange={ChangeLink}/>
            <Popup list={valList} vision={vision} setVision={setVision}/>
        </div>
    );
};

export default ImageLoader;