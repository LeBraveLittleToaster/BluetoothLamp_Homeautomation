package de.pschiessle.klight.backend.cli

import com.github.ajalt.clikt.core.CliktCommand
import com.github.ajalt.clikt.parameters.options.default
import com.github.ajalt.clikt.parameters.options.option

class CliCommands : CliktCommand() {

    val config : String by option(help="Path to config file").default("")

    override fun run() {
        println("Config Path = $config")
    }

}