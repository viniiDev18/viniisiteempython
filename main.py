import streamlit as st


@st.dialog("<3")
def caixa_modal(texto):
    st.write(texto)
@st.dialog("Você aceita ser minha princesa pro resto da vida?🥰")
def pedido_namoro():
    if st.button("Sim", use_container_width= True):
        st.write('Te amo minha linda❤️')
# Using "with" notation
with st.sidebar:
    # Fotos de vocês dois aqui <3
    st.header("Colecionando memórias ❤️", divider= "blue")
    st.image("conversa 2-735.jpg",
             caption='(15 de agosto de 2024) No meu aniversário me deparei com essa sua mensagem me parabenizando. Logo me veio uma memória de que havia apertado sua mão naquele dia em um culto na Sede, onde ainda não nos falavamos, mas acredito que ali seria um incentivo para o ínicio de nossa história...❤️')
    st.header("", divider= "blue")
    st.image("conversa1-735.jpg",
             caption='(17 de agosto de 2024) Aqui onde tudo começou, dois dias após meu aniversário, você comentou na postagem do nosso laion, e quem diria que a partir daí tudo começaria a mudar na nossas vidas, as batidas do meu coração elevaram a cada minuto que falava com você e ali mesmo demonstramos o nosso interesse um pelo outro, a partir dali começei a apresentar você ao Senhor nas minhas orações mais sinceras...❤️')
    st.header("", divider= "blue")
    st.image("foto-V&L-736px.png",
             caption='(19 de Outubro de 2024) O dia que nos vimos pela "primeira" vez em um Night Power na Sul, após alguns meses se falando por chat , te encontrei desde nosso primeiro aperto de mão com uma troca de sorrisos na inauguração da nova Logos Sede, neste dia (apesar de ciente do sentimento recíproco um pelo outro) eu ainda temia, pois estava receoso do que estava por acontecer, não estava tão esperançoso, mas neste dia a melhor parte do meu dia foi olhar nos seus olhos que brilhavam ao olhar para mim, eu os admirava, e a cada olhar neles eu podia ver minha face refletida em seus belos olhos e uma chama de esperança e amor se acendia dentro de mim...❤️')
    st.header("", divider= "blue")
    st.image("conversa3-735.jpg",
             caption='(25 de Dezembro de 2024) Aqui mandei uma mensagem de Feliz Natal para você, mandei essa mensagem pois já fazia meses sem nos falar. Como visto na mensagem ,durante este tempo, eu ainda não havia deixado o sentimento que tinha por você de lado, nunca o deixei e vi que era recíproco. A partir daí em diante através das nossas conversas eu vi que você foi a melhor coisa que me aconteceu nessa vida há muito tempo...❤️')
    st.header("", divider= "blue")
    st.image("foto_love-735.jpg",
             caption='(9 de Janeiro de 2025) Essa foto significa muito para mim, pois vejo que Deus sempre agiu em nossas vidas, nesse dia ele fez tudo perfeito, nos vimos depois de meses e com um sentimento certeiro e formado do amor que nos rodeia, ali já não estava mais inseguro do que sentia, mas sim a certeza de queria te amar até o fim dos séculos. Tive a oportunidade de conhecer seus pais e aumentar mais a vontade de fazer parte dessa família linda. Deixamos nossos pais conversando e isso me alegrou, pois enquanto eles se conheciam, tivemos a oportunidade de conversar face a face, pude olhar nos seus olhos que iluminavam minha alma, e sentir a leveza de sua prensença a mim, senti seu cheiro, batemos um bom papo, e ali a coisa começou a se desenrolar kkkk. Ali eu pude ter a certeza de que Deus já havia começado a escrever a nossa história juntos desde a fundação do mundo há milhares de anos atrás...❤️')
    st.header("", divider= "blue")
    st.image("recadinho_735px.png",
             caption='')
    st.header("", divider= "blue")
with st.container(border=True):
    st.header("Explore minha princesa😊❤️", divider="blue")
    st.subheader("Play na música que lembra a gente...🎶❤️")
    st.audio("Lied_To.mp3", format="audio/mpeg", loop=True)
    st.header("Aperte em cada '❤️' para explorar:", divider="blue")

    col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
    with col1:
        btn1 = st.button(
            "❤️",
            use_container_width= True, key=1)
        if btn1:
            caixa_modal('Você foi a melhor coisa que me aconteceu a muito tempo...💘')
    with col2:
        btn2 = st.button(
                "❤️",
                use_container_width=True, key=2)
        if btn2:
            caixa_modal('O que devo falar do seus olhos? O brilho dos seus olhos me fascinam, você me fascina garota!!💘')
    with col3:
        btn3 = st.button("❤️",
                use_container_width=True, key=3)
        if btn3:
            # Arrumar aqui
            caixa_modal('Estar com você me leva a um universo paralelo onde só existem você e eu...💘')
    with col4:
        btn4 = st.button(
                "❤️",
                use_container_width=True, key=4)
        if btn4:
            pedido_namoro()
    with col5:
        btn5 = st.button(
                "❤️",
                use_container_width=True, key=5)
        if btn5:
            caixa_modal('Você desperta a forte masculinidade que há dentro de mim, e me inspira a ser um homem de honra, eu te amo com todo o meu ser minha princesa!!🥰❤️')
    with col6:
        btn6 = st.button(
            "❤️",
            use_container_width=True, key=6)
        if btn6:
            caixa_modal('Te quero e te desejo a cada segundo que se passa...💘')
    with col7:
        btn7 = st.button(
            "❤️",
            use_container_width=True, key=7)
        if btn7:
            caixa_modal('Você é o amor da minha vida todinha🥰❤️')
    with col8:
        btn8 = st.button(
            "❤️",
            use_container_width=True, key=8)
        if btn8:
            caixa_modal('Vejo o brilho do Espírito Santo em você!!💖')