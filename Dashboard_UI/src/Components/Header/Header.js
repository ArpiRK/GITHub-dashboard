import React from "react";
import classes from "./header.module.css";

export default function Header() {
  const user = {
    name: "John",
  };
  const cart = { totalcount: 10 };
  return (
    <header classname={classes.header}>
      <div classname={classes.container}>
        <link to="/" classname={classes.logo}>
          Dashboard
        </link>
      </div>
    </header>
  );
}
