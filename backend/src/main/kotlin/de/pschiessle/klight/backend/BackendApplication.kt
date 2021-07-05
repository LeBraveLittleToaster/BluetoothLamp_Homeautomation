package de.pschiessle.klight.backend

import de.pschiessle.klight.backend.cli.CliCommands
import org.slf4j.Logger
import org.slf4j.LoggerFactory
import org.springframework.beans.factory.InjectionPoint
import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication
import org.springframework.boot.web.servlet.support.SpringBootServletInitializer
import org.springframework.context.annotation.Bean
import org.springframework.context.annotation.Configuration
import org.springframework.context.annotation.Scope


@SpringBootApplication
class BackendApplication

fun main(args: Array<String>) {
    CliCommands().main(args)
    runApplication<BackendApplication>(*args)
}
