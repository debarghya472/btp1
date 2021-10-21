import './Imageinsert.css'
import React from 'react';
import ImageUploading from 'react-images-uploading';

import { saveAs } from 'file-saver';


function filepath(img,name){


  saveAs(img, name)

}

function Navigation(){




const [images, setImages] = React.useState([]);
  const maxNumber = 69;


  const onChange = (imageList, addUpdateIndex) => {
    // data for submit
    console.log(imageList[0]);
    // filepath(imageList[0]['data_url'])
    setImages(imageList);
  };

  
  
  return (
    <div className="App">
      <ImageUploading
        multiple
        value={images}
        onChange={onChange}
        maxNumber={maxNumber}
        dataURLKey="data_url"
      >
        {({
          imageList,
          onImageUpload,
          onImageRemoveAll,
          onImageUpdate,
          onImageRemove,
          isDragging,
          dragProps,
        }) => (
          // write your building UI
          <div className="upload__image-wrapper">
            <button className="no-underline near-white bg-animate bg-navy hover-bg-near-black hover-gold inline-flex items-center ma2 tc br2 pa2 shadow-3 grow"
              style={isDragging ? { color: 'red' } : undefined}
              onClick={onImageUpload}
              {...dragProps}
            >
              Click or Drop here
            </button>
            <br/>
            &nbsp;
            
            {imageList.map((image, index) => (
              <div key={index} className="image-item">
                <img src={image['data_url']} alt="" width="250" height="auto" />
                
                <div className="image-item__btn-wrapper">
                <br/>
                  <div className="image-item__btn-wrapper">
                    <button className="no-underline near-white bg-animate bg-navy hover-bg-near-black hover-gold inline-flex items-center ma2 tc br2 pa2 shadow-3 grow" onClick={() => onImageRemove(index)}>Remove</button>
                  </div>
                  <ul>
                    <li><span  onClick={() => filepath(images[0]['data_url'],images[0].file['name'])}>Upload</span></li>
                  </ul>  
                  {/* <form action='/predict' method=["GET","POST"]>
                    <label>
                      Name of the File :
                      <input type="text" name="name" />
                    </label>
                    <input type="submit" value="Predict" />
                  </form> */}
                </div>
              </div>
            ))}
          </div>
        )}
      </ImageUploading>
    </div>
  );
}

export default Navigation;