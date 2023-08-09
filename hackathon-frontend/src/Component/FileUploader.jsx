import React, { useState } from 'react';
import Dropzone from 'react-dropzone';

const FileUploader = ({ onFileUpload }) => {
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileDrop = (acceptedFiles) => {
    setSelectedFile(acceptedFiles[0]);
  };

  const handleFileSubmit = () => {
    executePythonScript();
    if (selectedFile) {
      onFileUpload(selectedFile);
      
    }
    
  };
  const executePythonScript = async () => { 
    alert("file submitted successfully and python script is executed successfully");
    try {
      const response = await fetch('http://127.0.0.1:5000/execute-python', {
        method: 'GET',
      }); 
  
      if (response.ok) {
        console.log('Python script executed successfully.');
      }
    } catch (error) {
      console.error('Error executing Python script:', error);
    }
  };

  return (
    <div>
      <Dropzone onDrop={handleFileDrop} accept=".pdf">
        {({ getRootProps, getInputProps }) => (
          <div className="dropzone" {...getRootProps()}>
            <input {...getInputProps()} />
            <p>Drag and drop a PDF file here, or click to select one.</p>
          </div>
        )}
      </Dropzone>
      <button onClick={handleFileSubmit}>Start</button>   
    </div>
  );
};

export default FileUploader;




