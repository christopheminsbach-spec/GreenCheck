import { useState } from "react";

const API = "http://localhost:8000";


function App() {

  const [page, setPage] = useState("home");
  const [menu, setMenu] = useState(false);

  const [user, setUser] = useState(() => {
    const token = localStorage.getItem("token");
    return token
      ? { email: localStorage.getItem("email") }
      : null;
  });

  const [email,setEmail] = useState("");
  const [password,setPassword] = useState("");

  const [plants,setPlants] = useState([]);

  const [country,setCountry] = useState("");


  async function loadPlants(){

    const res = await fetch(
      `${API}/data?limit=20`
    );

    const data = await res.json();

    setPlants(data);

    setPage("results");

  }



  async function searchCountry(){

    if(!country)return;


    const res = await fetch(
      `${API}/country/${country}`
    );


    const data = await res.json();

    setPlants(data);

    setPage("results");

  }




  function login(e){

    e.preventDefault();


    localStorage.setItem(
      "token",
      "fake-jwt-token"
    );


    localStorage.setItem(
      "email",
      email
    );


    setUser({
      email
    });


    setPage("home");

  }




  function register(e){

    e.preventDefault();


    alert(
      "Inscription réussie"
    );


    setPage("login");

  }



  function logout(){

    localStorage.clear();

    setUser(null);

    setPage("home");

  }





return (

<div className="min-h-screen bg-gray-100">


<header className="bg-green-700 text-white p-5 flex justify-between">


<h1 className="text-3xl font-bold">
🌱 Planet Flora
</h1>



<nav className="flex gap-4 items-center">


<button
onClick={()=>setPage("home")}
>
Accueil
</button>



<div className="relative">


<button
className="bg-green-900 px-4 py-2 rounded"
onClick={()=>setMenu(!menu)}
>
API ▼
</button>



{
menu &&

<div className="absolute bg-white text-black mt-2 rounded shadow w-64 p-3">


<button
className="block p-2 w-full text-left"
onClick={loadPlants}
>
📊 Données plantes
</button>



<button
className="block p-2 w-full text-left"
onClick={()=>setPage("species")}
>
🌱 Identifier une espèce
</button>



<button
className="block p-2 w-full text-left"
onClick={()=>setPage("disease")}
>
🦠 Identifier une maladie
</button>



<button
className="block p-2 w-full text-left"
onClick={()=>setPage("variety")}
>
🌿 Identifier une variété
</button>



<button
className="block p-2 w-full text-left"
onClick={()=>setPage("country")}
>
🌍 Recherche pays
</button>


</div>

}


</div>



{
user ?

<>

<span>
{user.email}
</span>


<button
className="bg-red-500 px-3 rounded"
onClick={logout}
>
Déconnexion
</button>

</>

:

<>

<button
onClick={()=>setPage("login")}
>
Connexion
</button>


<button
onClick={()=>setPage("register")}
>
Inscription
</button>

</>

}



</nav>

</header>





{
page==="home" &&

<section className="
relative
overflow-hidden
min-h-[calc(100vh-90px)]
flex
items-center
justify-center
px-6
">


<div className="
absolute
inset-0
bg-gradient-to-br
from-green-100
via-white
to-emerald-200
">


</div>



<div className="
relative
max-w-6xl
grid
md:grid-cols-2
gap-12
items-center
">


<div>


<h2 className="
text-5xl
md:text-7xl
font-black
leading-tight
gradient-text
">

Planet Flora

</h2>


<p className="
mt-6
text-xl
text-gray-700
max-w-xl
">

L'intelligence artificielle au service
de la reconnaissance végétale.
Identifiez les espèces, maladies et
variétés en quelques secondes.

</p>



<div className="
mt-8
flex
flex-wrap
gap-4
">


<button

onClick={loadPlants}

className="
px-8
py-4
rounded-full
bg-green-600
text-white
font-bold
shadow-xl
hover:bg-green-700
hover:scale-105
transition
"

>

Explorer les plantes 🌱

</button>



<button

onClick={()=>setPage("species")}

className="
px-8
py-4
rounded-full
border
border-green-600
text-green-700
hover:bg-green-100
transition
"

>

Identifier une plante 📸

</button>


</div>



<div className="
grid
grid-cols-3
gap-4
mt-10
">


<div className="
bg-white
rounded-2xl
p-4
shadow
card-hover
">

🌱
<p className="font-bold">
Espèces
</p>

</div>



<div className="
bg-white
rounded-2xl
p-4
shadow
card-hover
">

🦠
<p className="font-bold">
Maladies
</p>

</div>




<div className="
bg-white
rounded-2xl
p-4
shadow
card-hover
">

🌿
<p className="font-bold">
Variétés
</p>

</div>



</div>


</div>





<div className="
hidden
md:flex
justify-center
">


<div className="
w-96
h-96
rounded-full
bg-gradient-to-br
from-green-400
to-emerald-700
shadow-2xl
flex
items-center
justify-center
text-9xl
float
">

🌳

</div>


</div>



</div>


</section>

}





{
page==="login" &&

<AuthForm

title="Connexion"

action={login}

email={email}

setEmail={setEmail}

password={password}

setPassword={setPassword}

/>

}





{
page==="register" &&

<AuthForm

title="Inscription"

action={register}

email={email}

setEmail={setEmail}

password={password}

setPassword={setPassword}

/>

}






{
page==="country" &&

<div className="p-10 text-center">

<h2 className="text-3xl mb-5">
Recherche par pays
</h2>


<input

className="border p-3"

placeholder="France"

value={country}

onChange={
e=>setCountry(e.target.value)
}

/>


<button

className="bg-green-600 text-white p-3 ml-3"

onClick={searchCountry}

>
Chercher
</button>


</div>

}







{
["species","disease","variety"].includes(page)

&&

<Scanner

type={page}

/>

}







{
page==="results"

&&

<div className="p-8 grid md:grid-cols-3 gap-5">


{

plants.map((p,i)=>(


<div
key={i}
className="bg-white p-5 rounded shadow"
>


<h3 className="font-bold">
{p.title || "Plante"}
</h3>


<p>
Pays : {p.country}
</p>


<p>
Prix : {p.price || "N/A"}
</p>


</div>


))

}


</div>

}



</div>

);


}







function AuthForm({

title,

action,

email,

setEmail,

password,

setPassword

}){


return (

<div className="p-10 flex justify-center">


<form

onSubmit={action}

className="bg-white p-8 shadow rounded w-96"

>


<h2 className="text-3xl mb-5">
{title}
</h2>



<input

className="border p-3 w-full mb-3"

placeholder="Email"

value={email}

onChange={
e=>setEmail(e.target.value)
}

/>



<input

className="border p-3 w-full mb-3"

type="password"

placeholder="Mot de passe"

value={password}

onChange={
e=>setPassword(e.target.value)
}

/>



<button

className="bg-green-600 text-white p-3 w-full"

>
Valider
</button>


</form>


</div>

)

}








function Scanner({type}){


const [file,setFile]=useState(null);

const [preview,setPreview]=useState(null);

const [result,setResult]=useState(null);

const [loading,setLoading]=useState(false);





function selectImage(e){


const img =
e.target.files[0];


setFile(img);



if(img){

setPreview(
URL.createObjectURL(img)
);

}


}





async function send(e){


e.preventDefault();


if(!file)
return;



setLoading(true);



const form =
new FormData();



form.append(
"image",
file
);





const res =
await fetch(

`${API}/api/identify/${type}`,

{

method:"POST",

body:form

}

);



const data =
await res.json();



console.log(
"API RESULT",
data
);



setResult(data);



setLoading(false);


}






return (

<div className="
p-8
grid
md:grid-cols-2
gap-8
">


<div className="
bg-white
rounded-3xl
shadow-xl
p-6
">


<h2 className="
text-3xl
font-bold
text-green-700
">

🌱 Identification

</h2>




<input

type="file"

accept="image/*"

onChange={selectImage}

/>




{
preview &&

<img

src={preview}

alt="plante"

className="
mt-5
rounded-2xl
w-full
h-80
object-cover
"

/>

}




<button

onClick={send}

className="
mt-5
bg-green-600
text-white
px-8
py-3
rounded-full
"

>


{
loading

?

"Analyse..."

:

"Analyser"

}


</button>



</div>






<div className="
bg-white
rounded-3xl
shadow-xl
p-6
">


<h2 className="
text-3xl
font-bold
">

Diagnostic

</h2>





{
result &&

<>


<h3 className="
text-2xl
font-bold
text-green-700
mt-4
">

{result.plante}

</h3>




<p>

Famille :

<b>
{result.famille}
</b>

</p>



<p>

Genre :

<b>
{result.genre}
</b>

</p>





<h3 className="mt-5 font-bold">

Noms communs

</h3>



<ul>

{

result.noms_communs?.map(

(n,i)=>(

<li key={i}>

🌿 {n}

</li>

)

)

}

</ul>





<div className="
mt-6
bg-green-100
rounded-xl
p-5
text-center
text-xl
">


Confiance :

<b>

{
result.confiance !== undefined

?

result.confiance

:

0

}

%

</b>


</div>




</>


}



</div>


</div>


)

}



export default App;