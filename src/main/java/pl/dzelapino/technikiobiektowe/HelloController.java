package pl.dzelapino.technikiobiektowe;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {

    // Basic GET request that returns a simple message
    @GetMapping("/hello")
    public String sayHello() {
        return "Hello, World!";
    }

    // GET request with a query parameter
    @GetMapping("/greet")
    public String greetUser(@RequestParam(value = "name", defaultValue = "Guest") String name) {
        return "Hello, " + name + "!";
    }

}
