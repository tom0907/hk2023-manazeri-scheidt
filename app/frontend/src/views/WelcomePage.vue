<template>
  <div class="main-menu">
    <div class="weather">
      <div>{{ weather.weather_desc }}</div>
      <div style="font-size: 2.5rem;">{{ weather.temp }}°C</div>
      <div>{{$t("WelcomePage.Humidity")}} {{ weather.humidity }}%</div>
    </div>

    <div background-color="red">
      <label class="start-finish-labels">{{$t("WelcomePage.Start")}}</label><br />
      <input class="menu-input" type="text" v-model="first"/><br />
      <label class="start-finish-labels">{{$t("WelcomePage.Destination")}}</label><br />
      <input class="menu-input" type="text" v-model="second"/><br />
    </div>

    <div class="menu-radio">
      <input type="radio" id="radio1" name="radio" value="-auto" v-model="radio"/>
      <label for="radio1">{{$t("WelcomePage.Car")}}</label><br />
      <input type="radio" id="radio2" name="radio" value="-mhd" v-model="radio" />
      <label for="radio2">{{$t("WelcomePage.PublicTransport")}}</label><br />
      <input type="radio" id="radio3" name="radio" value="" v-model="radio"/>
      <label for="radio3">{{$t("WelcomePage.OnFoot")}}</label><br />
    </div>

    <div>
      <label class="start-finish-labels" style="margin:4px">{{$t("WelcomePage.Services")}}</label><br />
      <select name="locations" v-model="select">
        <option value="cafe">{{$t("WelcomePage.Cafe")}}</option>
        <br />
        <option value="bar">{{$t("WelcomePage.Bar")}}</option>
        <option value="hospital">{{$t("WelcomePage.Hospital")}}</option>
        <option value="school">{{$t("WelcomePage.School")}}</option>
        <option value="bank">{{$t("WelcomePage.Bank")}}</option>
        <option value="pharmacy">{{$t("WelcomePage.Pharmacy")}}</option>
        <option value="supermarket">{{$t("WelcomePage.Supermarket")}}</option>
        <option value="fast_food">{{$t("WelcomePage.FastFood")}}</option>
        <option value="cinema">{{$t("WelcomePage.Cinema")}}</option>
        <option value="fuel">{{$t("WelcomePage.GasStation")}}</option>
      </select>
    </div>
  </div>
  <button class="menu-button" @click="navigate()">{{$t("WelcomePage.Go")}}</button>


  <div v-if="this.switch">
    <hr class="hr-line" />

    <div>
      <img
        :src="PhotoPath + this.first + temp + this.second + this.radio + format"
        class="map"
      />
    </div>

    <hr class="hr-line" />
    <div style="float: center; text-align: center">{{$t("WelcomePage.BusLines")}}</div>
    <br />
    <div class="links">
      <div class="linka" v-for="item in zastavky" :key="item.id">
        {{ item }}
      </div>
    </div>
    <hr class="hr-line" />
    <div class="main-menu" style="margin: 0% 30% 0 30%">
      <div>
        {{$t("WelcomePage.BusStops")}}<br /><br />
        <p v-for="item in stations" :key="item.id">{{ item.Alpinka }}</p>
      </div>
      <div>
        {{$t("WelcomePage.ServicesOnRoute")}}<br /><br />
        <p v-for="item in amenity" :key="item.id">
          {{ item.tags.name }}
        </p>
      </div>
    </div>
  </div>
</template>



<script>
import axios from "axios";

export default {
  name: "welcompage",
  components: {},
  data() {
    return {
      weather: [],
      PhotoPath: "http://127.0.0.1:8000/Photos/",
      switch: false,
      stations: [],
      buslines: [],
      amenity: [],
      temp: "-",
      format: ".png",
      zastavky: ["27", "36", "10", "54", "51"],
    };
  },
  methods: {
    getWeather() {
      axios.get("http://127.0.0.1:8000/weather").then((response) => {
        this.weather = response.data;
      });
    },
    getPicture() {
      axios
        .get("http://127.0.0.1:8000/Photos/furca-jazero.png")
        .then((response) => {
          this.weather = response.data;
        });
    },
    getAmenity() {
      axios
        .get("http://127.0.0.1:8000/amenity/" + this.select)
        .then((response) => {
          this.amenity = response.data[this.select];
          console.log(this.amenity[this.select]);
          console.log(this.amenity.cafe);
        });
    },
    getMHD() {
      axios
        .get("http://127.0.0.1:8000/stations/" + this.second)
        .then((response) => {
          this.stations = response.data;
        });
      axios.get("http://127.0.0.1:8000/buslines").then((response) => {
        this.buslines = response.data;
      });
    },
    navigate() {
      this.switch = true;
      this.getAmenity();
      this.getMHD();
    },
  },
  mounted: function () {
    //this.getWeather();
  },
};
</script>

<style>
.linka {
  color: white;
  font-weight: bolder;
  background-color: #00aba5;
  border-radius: 5px;
  padding: 8px;
}
.links {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  margin: 0% 30% 0 30%;
}
.hr-line {
  width: 70%;
  text-align: left;
  margin-top: 2rem;
  margin-bottom: 2rem;
  border: 1px solid #e4032f;
}
.map {
  display: block;
  margin: auto;
  border: 2px solid #e4032f;
  border-radius: 3%;
  width: 60%;
}
select {
  appearance: none;
  border: 2px solid #ccc;
  border-radius: 5px;
  font-size: 16px;
  padding: 8px 12px;
  width: 200px;
  background-color: #fff;
  background-position: right 10px center;
  background-repeat: no-repeat;
  cursor: pointer;
}
input[type="radio"] {
  appearance: none;
  display: inline-block;
  padding: 10px;

  border: 2px solid #ccc;
  border-radius: 50%;
  margin: 6px;
  vertical-align: middle;
  cursor: pointer;
}

input[type="radio"]:checked {
  background-color: #00aba5;
  border-color: #00aba5;
}

input[type="radio"]:hover:not(:checked) {
  border-color: #888;
}

.weather {
  border: 2px solid #017bc5;
  border-radius: 10px;
  padding: 10px;
  color: black;
  text-align: center;
}
input {
  padding: 1rem;
  margin-bottom: 1rem;
}
.main-menu {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  border-radius: 5px;
  margin: 7% 20% 0 20%;
}

/* Set styles for the input fields and button in the middle */
.menu-input {
  flex: 1;
  margin-right: 10px;
  margin-top: 4px;
  padding: 5px;
  border: none;
  background-color: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  border-radius: 5px;
}

.menu-button {
  padding: 5px 10px;
  background-color: #007ac7;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  width: 150px;
  height: 40px;
  display: block;
  margin: auto;
}
.menu-button:hover {
  background-color: rgb(52, 112, 158);
}

/* Set styles for the radioes on the right */
</style>
