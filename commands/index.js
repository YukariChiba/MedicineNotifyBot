import Subscribe from "./Subscribe.js";
import Unubscribe from "./Unsubscribe.js";
import Info from "./Info.js";
import List from "./List.js";

var cmdList = [];

cmdList = cmdList.concat(Subscribe);
cmdList = cmdList.concat(Unubscribe);
cmdList = cmdList.concat(Info);
cmdList = cmdList.concat(List);

export default cmdList;
