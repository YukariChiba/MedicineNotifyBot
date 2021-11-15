import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const basename = path.basename(fileURLToPath(import.meta.url));
const dirname = path.dirname(fileURLToPath(import.meta.url));
let cmdList = [];

let moduleFiles = fs
  .readdirSync(dirname)
  .filter(
    (file) =>
      file.indexOf(".") !== 0 && file !== basename && file.slice(-3) === ".js"
  );

for (let moduleFile of moduleFiles) {
  await import(path.join(dirname, moduleFile)).then((module) => {
    cmdList = cmdList.concat(module.default);
  });
}

export default cmdList;
