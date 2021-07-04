import org.springframework.beans.factory.annotation.Autowired
import org.springframework.context.annotation.Bean
import org.springframework.stereotype.Component
import org.springframework.web.reactive.HandlerMapping
import org.springframework.web.reactive.handler.SimpleUrlHandlerMapping
import org.springframework.web.reactive.socket.WebSocketHandler
import org.springframework.web.reactive.socket.WebSocketMessage
import org.springframework.web.reactive.socket.WebSocketSession
import reactor.core.publisher.Mono
import reactor.core.publisher.Sinks
import java.util.*
import javax.annotation.PostConstruct

class ReactiveWebSocketHandler() : WebSocketHandler {

    final val sink: Sinks.Many<String> = Sinks.many().replay().all()
    val flux = sink.asFlux()

    @PostConstruct
    fun iamAlive() {
        println("Hello AppEcosystemController")
    }

    override fun handle(webSocketSession: WebSocketSession): Mono<Void> {
        return webSocketSession.send(
            flux
                .map(webSocketSession::textMessage)
        )
            .and(
                webSocketSession.receive()
                    .map(WebSocketMessage::getPayloadAsText)
                    .log()
            )
    }
}

