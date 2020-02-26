<!--title={the Debugger}--> 

Using the statement `Debugger;` in Node.js or Express.js is similar to using `Console.log()` but more powerful in some ways. 



The **Chrome 5** browser's debugger is designed specifically for Node.js and Express.js, but any browser has tools that work with the Debugger. The following steps are the process to use the Chrome debugger (and similarly for other web browsers, although the general concepts will be the same): 

1. Create your program with `Debugger;` statements. Lines with the `Debugger;` statement will be integrated into the Chrome Debugger. 

2. Run your program through the terminal using the keyword `inspect`. The line will be similar to this:

   ```
   node inspect yourProgramHere
   ```

3. Type in your browser `chrome://inspect`. If you've already run your program, there should be two items under **Remote Target**. The two items should be duplicates of eachother. 

   ![picture](/Users/nathankong/Desktop/Screen Shot 2019-12-01 at 1.08.31 PM.png)

   If you don't see anything, your browser may be misconfigured. To configure your browser, click **configure** and add `localhost:9229` and `127.0.0.1:9229`. Then refresh the page. 

4. If you click **inspect**, a new browser window should pop up with the Chrome devtools. If you click the **play icon** execution will begin. Execution will be stopped at each `Debugger;` line. To resume execution click the **play icon** again. 

5. Once your program has completed execution, you need to type `debugger restart` from the terminal to restart the process



The Debugger has numerous tools. If you press the **play icon** the console will show your code on the left, and variables on the right. 

1. **Watch** shows current values for any expressions
2. **Call Stack** shows the current call chain
3. **Scope** shows local and global variables. 
4. If you press `escape` , the `console` shows up. You can type variables, and the `console` will return the present state of the variables. 