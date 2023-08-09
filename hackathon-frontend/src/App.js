import React from 'react';
import FileUploader from './Component/FileUploader';
import './App.css';

function App() {
  const handleFileUpload = async (file) => {

    const fileUrl = URL.createObjectURL(file);
    window.open(fileUrl);

  };

  return (
    <div className="App">
      <h1>Upload File Here... </h1>
      <FileUploader onFileUpload={handleFileUpload} />
    </div>
  );
}

export default App;




