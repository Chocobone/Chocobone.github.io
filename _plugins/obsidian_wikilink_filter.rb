Jekyll::Hooks.register [:posts, :pages], :pre_render do |post|
  # 이미지 Wikilink 변환: ![[image.png]] -> <img src="/assets/images/image.png">
  # 크기 조절 대응: ![[image.png|300]] -> <img src="/assets/images/image.png" width="300">
  post.content.gsub!(/!\[\[(.*?)\]\]/) do |match|
    content = $1.split('|')
    path = content[0].strip
    width = content[1] ? " width=\"#{content[1].strip}\"" : ""

    # 여기서 "/assets/images/"는 실제 이미지가 저장되는 경로에 맞게 수정하세요.
    "<img src=\"/assets/images/#{path}\"#{width} alt=\"#{path}\">"
  end

  # 일반 문서 링크 변환: [[Internal Link]] -> [Internal Link](/internal-link)
  post.content.gsub!(/\[\[(.*?)\]\]/) do |match|
    content = $1.split('|')
    name = content[1] || content[0]
    url = content[0].strip.downcase.gsub(' ', '-')
    "<a href=\"#{url}\">#{name}</a>"
  end
end
