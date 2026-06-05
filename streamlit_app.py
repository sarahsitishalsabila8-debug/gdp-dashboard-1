<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Database Bahan Kimia</title>

<style>
body{
    font-family: Arial, sans-serif;
    background:#f4f4f4;
    margin:20px;
}

h1{
    text-align:center;
    color:#003366;
}

#search{
    width:100%;
    padding:10px;
    margin-bottom:20px;
    border-radius:5px;
    border:1px solid #ccc;
}

table{
    width:100%;
    border-collapse:collapse;
    background:white;
}

th{
    background:#003366;
    color:white;
    padding:10px;
}

td{
    border:1px solid #ddd;
    padding:10px;
    text-align:center;
}

img{
    width:80px;
    height:auto;
}

button{
    background:#007bff;
    color:white;
    border:none;
    padding:8px 12px;
    border-radius:5px;
    cursor:pointer;
}

button:hover{
    background:#0056b3;
}
</style>
</head>
<body>

<h1>DATABASE BAHAN KIMIA</h1>

<input type="text" id="search" placeholder="Cari nama bahan...">

<table id="chemicalTable">
<thead>
<tr>
<th>Nama Bahan</th>
<th>Rumus Kimia</th>
<th>Struktur Kimia</th>
<th>Simbol Bahaya</th>
<th>Gambar Bahan</th>
<th>MSDS</th>
</tr>
</thead>

<tbody>

<tr>
<td>Asam Klorida</td>
<td>HCl</td>
<td><img src="struktur/hcl.png"></td>
<td><img src="simbol/korosif.png"></td>
<td><img src="gambar/hcl.jpg"></td>
<td>
<a href="msds/MSDS_Asam_Klorida.pdf" target="_blank">
<button>Lihat MSDS</button>
</a>
</td>
</tr>

<tr>
<td>Asam Sulfat</td>
<td>H₂SO₄</td>
<td><img src="struktur/h2so4.png"></td>
<td><img src="simbol/korosif.png"></td>
<td><img src="gambar/h2so4.jpg"></td>
<td>
<a href="msds/MSDS_Asam_Sulfat.pdf" target="_blank">
<button>Lihat MSDS</button>
</a>
</td>
</tr>

<tr>
<td>Asam Oksalat</td>
<td>H₂C₂O₄</td>
<td><img src="struktur/oksalat.png"></td>
<td><img src="simbol/iritan.png"></td>
<td><img src="gambar/oksalat.jpg"></td>
<td>
<a href="msds/MSDS_Asam_Oksalat.pdf" target="_blank">
<button>Lihat MSDS</button>
</a>
</td>
</tr>

<tr>
<td>Asam Nitrat</td>
<td>HNO₃</td>
<td><img src="struktur/hno3.png"></td>
<td><img src="simbol/oksidator.png"></td>
<td><img src="gambar/hno3.jpg"></td>
<td>
<a href="msds/MSDS_Asam_Nitrat.pdf" target="_blank">
<button>Lihat MSDS</button>
</a>
</td>
</tr>

<tr>
<td>Kalium Hidroksida</td>
<td>KOH</td>
<td><img src="struktur/koh.png"></td>
<td><img src="simbol/korosif.png"></td>
<td><img src="gambar/koh.jpg"></td>
<td>
<a href="msds/MSDS_KOH.pdf" target="_blank">
<button>Lihat MSDS</button>
</a>
</td>
</tr>

</tbody>
</table>

<script>
const search = document.getElementById("search");

search.addEventListener("keyup", function() {

let filter = search.value.toLowerCase();

let rows = document.querySelectorAll("#chemicalTable tbody tr");

rows.forEach(row => {

let text = row.textContent.toLowerCase();

if(text.includes(filter)){
row.style.display = "";
}else{
row.style.display = "none";
}

});

});
</script>

</body>
</html>
