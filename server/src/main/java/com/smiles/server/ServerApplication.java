package com.smiles.server;

import com.smiles.server.controller.DataCatImpl;
import com.smiles.server.controller.MoleculeImpl;
import io.grpc.Server;
import io.grpc.ServerBuilder;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import java.io.IOException;

@SpringBootApplication
public class ServerApplication {

    public static void main(String[] args) throws IOException, InterruptedException {

        SpringApplication.run(ServerApplication.class, args);
        int localport = 50051;
        Server server = ServerBuilder
            .forPort(localport)
            .addService(new MoleculeImpl())
            .build();
        server.start();

        Runtime.getRuntime()
            .addShutdownHook(
                new Thread(() -> {
                    try {
                        Thread.sleep(1000);
                        System.out.println("\n \nReceived Shutdown Request");
                        Thread.sleep(1000);
                        server.shutdown();
                        System.out.println(
                            "\n -> -> -> Successfully stopped the gRPC services <- <- <-"
                        );
                    } catch (InterruptedException e) {
                        throw new RuntimeException(e);
                    }
                })
            );
        server.awaitTermination();
    }
}
