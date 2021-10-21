
import './App.css';
// import Navigation from "./Components/Navigation/Navigation";
import Logo from "./Components/Logo/Logo";
import Imageinsert from "./Components/Imageinsert/Imageinsert";
import Particles from 'react-particles-js';
import Predict from "./Components/Predict/Predict";



function App() {
  return (
    <div className="App">
      {/*<Navigation />*/}
      <Logo />
      <Imageinsert/>
      <Particles 
                params={{
                    polygon: {
                        enable: true,
                        type: 'outside',
                        move: {
                            radius: 50
                        },
                        
                        
                    }
                }} />
      <Predict/>
    </div>
  );
}

export default App;
