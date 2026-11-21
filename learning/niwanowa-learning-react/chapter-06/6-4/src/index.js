import React, { createContext } from "react";
import colors from "./color-data.json";
import { createRoot } from "react-dom/client";
import App from "./App";

export const ColorContext = createContext();

const root = createRoot(document.getElementById("root"));
root.render(
    <ColorContext.Provider value={{ colors }}>
        <App />
    </ColorContext.Provider>
);