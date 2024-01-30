import {useState, useEffect} from "react";

export default function Home() {
  const [data, setData] = useState();
  const { data: userData, error: userError, handleLogin } = useLogin();

  const handleForm = (e) => {
    e.preventDefault();
    const form = e.currentTarget;
    const formData = new FormData(form);
    const { user, pw } = Object.fromEntries(formData);
    handleLogin({ user: user, pw: pw });
    window.location.href='/';
  };

  return (
    <div>
      <div className="flex w-full items-center flex-col absolute top-60" >
      
        <form onSubmit={handleForm}>
          <div className="border border-black flex flex-col p-6 space-y-2 bg-slate-200">
            <label>
              <input name="user" type="text" placeholder="User name" className="p-2"/>
            </label>
            <label>
              <input name="pw" placeholder="Password" type="text" className="p-2" />
            </label>
            <button type="submit" className="bg-blue-400 text-white p-2 mt-2" > 
              Submit
            </button>
          </div>
        </form>
        </div>
        </div>
  );
}

const useLogin = () => {
  const [data, setData] = useState();
  const [error, setError] = useState();
  const handleLogin = async ({user, pw}) => {
    console.log(user);
    try {
      const data = await fetch("http://localhost:5001/login", {
        method: "POST", 
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username: user, password: pw }),
      }).then((res) => res.json());

      setData(data);
      console.log(data);
    } catch (e) {
      console.log(e);
      setError(e.data);
    }
  };

  return {data, handleLogin, error};
}

