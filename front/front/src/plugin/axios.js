import axios from "axios";

// const instance = axios.create({
//   baseURL: "https://jsonplaceholder.typicode.com",
//   headers: { "X-Custom-Header": "foobar" },
// });

const instance = axios.create({
	baseURL: "https://yallashotalkora.com/api/",
	headers: { "Content-Type": "application/json; charset=UTF-8" },
});

export default instance;
